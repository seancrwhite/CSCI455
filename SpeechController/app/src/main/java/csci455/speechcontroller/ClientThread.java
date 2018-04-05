package csci455.speechcontroller;

import android.os.Handler;
import android.os.Message;

/**
 * Created by seancrwhite on 4/4/18.
 */

public class ClientThread extends Thread {
    String phrase;

    public ClientThread(){
        phrase = "";

        start();
    }

    @Override
    public void run() {
        while (true) {
            if (!phrase.equals("")) {
                RobotConnector robotConnector = RobotConnector.getInstance();
                robotConnector.send(phrase);
                phrase = "";
            }
        }
    }

    private final Handler handler = new Handler() {
        public void handleMessage(Message msg) {
            phrase = msg.getData().getString("client");
        }
    };

    public Handler getHandler() {
        return handler;
    }
}
