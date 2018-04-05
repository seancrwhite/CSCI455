package csci455.speechcontroller;

import android.os.Bundle;
import android.os.Message;

/**
 * Created by seancrwhite on 4/2/18.
 */

public class ServerThread extends Thread {
    private MainActivity parent;

    public ServerThread(MainActivity parent){
        this.parent = parent;

        start();
    }

    @Override
    public void run() {
        RobotConnector robotConnector = RobotConnector.getInstance();

        while(true) {
            String phrase = robotConnector.receive();

            if (!phrase.equals("")) {
                Message msg = parent.handler.obtainMessage();

                Bundle bundle = new Bundle();
                bundle.putString("client", phrase);

                msg.setData(bundle);

                parent.handler.sendMessage(msg);
            }
        }
    }
}
