package csci455.robotcontroller;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button btn_talk = findViewById(R.id.btn_talk);
        btn_talk.setOnClickListener(this);
    }

    @Override
    public void onClick(View view) {
        Log.v("Button Press:", view.toString());

        Intent intent_talk = new Intent(this, TalkActivity.class);
        startActivity(intent_talk);
    }
}
