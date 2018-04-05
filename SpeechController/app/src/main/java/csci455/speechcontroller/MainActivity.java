package csci455.speechcontroller;

import android.content.Intent;
import android.os.Handler;
import android.os.Message;
import android.speech.RecognizerIntent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import java.net.Inet4Address;
import java.net.InetAddress;
import java.net.NetworkInterface;
import java.net.SocketException;
import java.util.ArrayList;
import java.util.Enumeration;
import java.util.Locale;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {
    EditText et_display_box;
    TextView tv_ip_addr;
    Button btn_record;
    Button btn_send;
    TextParser parser_txt;
    ServerThread server;
    ClientThread client;

    final int REQUEST_CODE = 10;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        et_display_box = findViewById(R.id.et_display_box);
        tv_ip_addr = findViewById(R.id.tv_ip_addr);
        btn_record = findViewById(R.id.btn_record);
        btn_send = findViewById(R.id.btn_send);

        btn_record.setOnClickListener(this);
        btn_send.setOnClickListener(this);

        parser_txt = new TextParser(this);
        server = new ServerThread(this);
        client = new ClientThread();
        
        tv_ip_addr.setText(getIpAddr());
    }

    public final Handler handler = new Handler() {
        public void handleMessage(Message msg) {
            String phrase = msg.getData().getString("client");
            et_display_box.setText(phrase);

            Handler tts_handler = parser_txt.getHandler();

            Message out_msg = tts_handler.obtainMessage();

            Bundle bundle = new Bundle();
            bundle.putString("client", phrase);

            out_msg.setData(bundle);

            tts_handler.sendMessage(out_msg);
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

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        switch (requestCode) {
            case REQUEST_CODE:
                if (resultCode == RESULT_OK && data != null) {
                    ArrayList<String> result = data.getStringArrayListExtra(RecognizerIntent.EXTRA_RESULTS);
                    et_display_box.setText(result.get(0));
                }
                break;
        }
    }

    @Override
    public void onClick(View view) {
        Log.v("Button Press:", view.toString());

        switch(view.getId()) {
            case R.id.btn_record:
                Intent intent = new Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH);
                intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM);
                intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, Locale.getDefault());

                if (intent.resolveActivity(getPackageManager()) != null) {
                    startActivityForResult(intent, REQUEST_CODE);
                } else {
                    Toast.makeText(this, "Your Device Don't Support Speech Input", Toast.LENGTH_SHORT).show();
                }

                break;

            case R.id.btn_send:
                String input = et_display_box.getText().toString();

                Bundle bundle = new Bundle();
                bundle.putString("client", input);

                Handler handler = client.getHandler();
                Message msg = handler.obtainMessage();

                msg.setData(bundle);
                handler.sendMessage(msg);
                System.out.println("Sent to client thread");

                break;
        }
    }
}
