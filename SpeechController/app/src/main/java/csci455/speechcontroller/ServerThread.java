package csci455.speechcontroller;

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
    private ServerSocket socket;

    public ServerThread(){
        port = 5000;
    }

    @Override
    public void run() {
        try {
            socket = new ServerSocket(port);

            while(true) {
                Socket client = socket.accept();

                BufferedReader in = new BufferedReader(new InputStreamReader(client.getInputStream()));
                String msg = in.readLine();

                System.out.println(msg);
            }
        }catch (IOException e) {
            e.printStackTrace();
        }
    }
}
