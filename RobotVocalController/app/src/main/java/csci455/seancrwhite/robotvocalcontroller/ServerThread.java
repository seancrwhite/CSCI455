package csci455.seancrwhite.robotvocalcontroller;

import android.os.Bundle;
import android.os.Message;

/**
 * Created by seancrwhite on 4/18/18.
 */

public class ServerThread extends Thread {
    private MainActivity parent;

    public ServerThread(MainActivity parent){
        this.parent = parent;

        start();
    }

    @Override
    public void run() {
        while(true) {
            RobotConnector robotConnector = RobotConnector.getInstance();

            if(robotConnector != null) {
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
}
