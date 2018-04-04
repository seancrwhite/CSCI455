package csci455.speechcontroller;

import android.os.Handler;
import android.os.Message;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

import java.net.Inet4Address;
import java.net.InetAddress;
import java.net.NetworkInterface;
import java.net.SocketException;
import java.util.Enumeration;

public class MainActivity extends AppCompatActivity {
    EditText et_display_box;
    TextView tv_ip_addr;
    SpeechParser parser_spch;
    TextParser parser_txt;
    ServerThread server;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        et_display_box = findViewById(R.id.et_display_box);
        tv_ip_addr = findViewById(R.id.tv_ip_addr);

        parser_spch = new SpeechParser();
        parser_txt = new TextParser(this);
        server = new ServerThread(this);
        
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
                        ipAddress=inetAddress.getHostAddress().toString();
                        return ipAddress;
                    }
                }
            }
        } catch (SocketException ex) {
            ex.printStackTrace();
        }
        return ipAddress;
    }
}
