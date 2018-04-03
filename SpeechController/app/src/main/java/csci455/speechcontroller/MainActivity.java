package csci455.speechcontroller;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {
    EditText text_display_box;
    SpeechParser parser_spch;
    TextParser parser_txt;
    ServerThread server;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        text_display_box = findViewById(R.id.text_display_box);
        parser_spch = new SpeechParser();
        parser_txt = new TextParser(this);
        server = new ServerThread();
    }
}
