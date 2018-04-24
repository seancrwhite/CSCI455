package csci455.seancrwhite.robotvocalcontroller;

import android.content.Intent;
import android.os.Handler;
import android.os.Message;
import android.speech.RecognizerIntent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

import java.net.Inet4Address;
import java.net.InetAddress;
import java.net.NetworkInterface;
import java.net.SocketException;
import java.util.ArrayList;
import java.util.Enumeration;
import java.util.Locale;

public class MainActivity extends AppCompatActivity {
    TTS tts;
    ClientThread thread_c;
    ServerThread thread_s;
    TextView ip_addr;

    final int REQUEST_CODE = 10;
    private boolean ttsIsSpeaking;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        tts = new TTS(this);

        thread_s = new ServerThread(this);
        thread_c = new ClientThread();

        ip_addr = findViewById(R.id.ip_addr);
        ip_addr.setText(getIpAddr());
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        switch (requestCode) {
            case REQUEST_CODE:
                if (resultCode == RESULT_OK && data != null) {
                    ArrayList<String> result = data.getStringArrayListExtra(RecognizerIntent.EXTRA_RESULTS);

                    Bundle bundle = new Bundle();
                    bundle.putString("client", result.get(0));

                    Handler handler = thread_c.getHandler();
                    Message msg = handler.obtainMessage();

                    msg.setData(bundle);
                    handler.sendMessage(msg);
                }
                break;
        }
    }

    @Override
    protected void onDestroy() {
        if(tts != null) {
            //tts.stop();
            tts.shutdown();
        }

        super.onDestroy();
    }

    public final Handler handler = new Handler() {
        public void handleMessage(Message msg) {
            String phrase = msg.getData().getString("client");

            Handler tts_handler = tts.getHandler();

            Message out_msg = tts_handler.obtainMessage();

            Bundle bundle = new Bundle();
            bundle.putString("client", phrase);

            out_msg.setData(bundle);

            tts_handler.sendMessage(out_msg);

            ttsIsSpeaking = true;
            while(ttsIsSpeaking) {
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }

            if(phrase.contains("Game over")) {
                return;
            }

            Intent intent = new Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH);
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM);
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, Locale.getDefault());

            startActivityForResult(intent, REQUEST_CODE);
        }
    };

    private String getIpAddr() {
        String ipAddress = "Unable to Fetch IP..";
        try {
            Enumeration en;
            en = NetworkInterface.getNetworkInterfaces();
            while ( en.hasMoreElements()) {
                NetworkInterface intf = (NetworkInterface)en.nextElement();
                for (Enumeration enumIpAddr = intf.getInetAddresses(); enumIpAddr.hasMoreElements();) {
                    InetAddress inetAddress = (InetAddress)enumIpAddr.nextElement();
                    if (!inetAddress.isLoopbackAddress()&&inetAddress instanceof Inet4Address) {
                        ipAddress = inetAddress.getHostAddress().toString();
                        return ipAddress;
                    }
                }
            }
        } catch (SocketException ex) {
            ex.printStackTrace();
        }
        return ipAddress;
    }

    public void setDoneSpeaking() {
        ttsIsSpeaking = false;
    }
}
