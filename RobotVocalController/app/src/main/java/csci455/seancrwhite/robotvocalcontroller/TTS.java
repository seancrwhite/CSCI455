package csci455.seancrwhite.robotvocalcontroller;

import android.content.Context;
import android.os.Handler;
import android.os.Looper;
import android.os.Message;
import android.speech.tts.TextToSpeech;
import android.util.Log;
import android.widget.Toast;

import java.util.Locale;

/**
 * Created by seancrwhite on 4/18/18.
 */

public class TTS extends Thread implements TextToSpeech.OnInitListener {
    private TextToSpeech tts;
    private MainActivity context;
    private String last;
    private Handler handler;

    public TTS(MainActivity context) {
        this.context = context;
        tts = new TextToSpeech(context, this);
        last = "";
    }

    @Override
    public void onInit(int status) {
        switch(status) {
            case TextToSpeech.SUCCESS:
                int result = tts.setLanguage(Locale.US);

                tts.setPitch(0);         // Change pitch
                tts.setSpeechRate(0);    // Change how fast it talks

                if(result == TextToSpeech.LANG_MISSING_DATA ||
                        result == TextToSpeech.LANG_NOT_SUPPORTED) {
                    Toast.makeText(context, "Language load error", Toast.LENGTH_LONG).show();
                }

                start();
                break;
        }
    }

    @Override
    public void run() {
        Looper.prepare();

        handler = new Handler() {
            public void handleMessage(Message msg) {
                String response = msg.getData().getString("client");

                Log.v("Response:", response);

                // Make robot talk
                convert(response);
            }
        };

        Looper.loop();
    }

    public void convert(String txt) {
        tts.speak(txt, TextToSpeech.QUEUE_FLUSH, null, null);

        while(tts.isSpeaking()) {
            try {
                Thread.sleep(200);

            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        context.setDoneSpeaking();
    }

    public boolean isSpeaking() {
        return tts.isSpeaking();
    }

    public void shutdown() {
        tts.shutdown();
    }

    public Handler getHandler() {
        return handler;
    }
}
