package csci455.speechcontroller;

import android.app.Activity;
import android.os.Bundle;
import android.os.Message;
import android.util.Log;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * Created by seancrwhite on 4/2/18.
 */

public class ServerThread extends Thread {
    private int port;
    private MainActivity parent;
    private ServerSocket socket;

    public ServerThread(MainActivity parent){
        port = 5000;
        this.parent = parent;
        start();
    }

    @Override
    public void run() {
        try {
            System.out.println("Connecting...");
            socket = new ServerSocket(port);
            Socket client = socket.accept();

            BufferedReader in = new BufferedReader(new InputStreamReader(client.getInputStream()));
            String phrase;

            System.out.println("Connection Established. Listening.");

            while(true) {
                phrase = in.readLine();

                if (phrase != null){
                    Log.v("LOGGING", phrase);

                    Message msg = parent.handler.obtainMessage();

                    Bundle bundle = new Bundle();
                    bundle.putString("client", phrase);

                    msg.setData(bundle);

                    parent.handler.sendMessage(msg);
                }
            }
        }catch (IOException e) {
            System.out.println("Server Error:");
            e.printStackTrace();
        }
    }
}
