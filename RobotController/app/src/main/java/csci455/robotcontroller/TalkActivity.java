package csci455.robotcontroller;

import android.os.Handler;
import android.os.Message;
import android.speech.tts.TextToSpeech;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class TalkActivity extends AppCompatActivity implements View.OnClickListener {
    EditText txt_output;
    TTS tts;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_talk);

        txt_output = findViewById(R.id.txt_output);

        Button btn_record = findViewById(R.id.btn_record);
        btn_record.setOnClickListener(this);

        tts = new TTS(this);
        tts.start();
    }

    @Override
    public void onClick(View view) {
        Log.v("Button Press:", view.toString());

        switch(view.getId()) {
            case R.id.btn_record:
                String input = txt_output.getText().toString();

                Bundle bundle = new Bundle();
                bundle.putString("TT", input);

                Handler handler = tts.getHandler();
                Message msg = handler.obtainMessage();

                msg.setData(bundle);
                handler.sendMessage(msg);

                break;
        }
    }
}
