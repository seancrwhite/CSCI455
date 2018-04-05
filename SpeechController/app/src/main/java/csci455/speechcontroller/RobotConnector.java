package csci455.speechcontroller;

import android.util.Log;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * Created by seancrwhite on 4/4/18.
 */

public class RobotConnector {
    private static RobotConnector instance;
    private static int port = 5000;
    private static Socket connection;

    private RobotConnector(Socket connection){
        this.connection = connection;
    }

    public static RobotConnector getInstance() {
        if (instance == null) {
            try {
                System.out.println("Connecting...");
                ServerSocket socket = new ServerSocket(port);
                Socket connection = socket.accept();

                System.out.println("Connection Established. Listening.");

                instance = new RobotConnector(connection);
            } catch (IOException e) {
                System.out.println("Connection Error:");
                e.printStackTrace();
            }
        }

        return instance;
    }

    public void send(String phrase) {
        try {
            OutputStream out = connection.getOutputStream();
            PrintWriter output = new PrintWriter(out);

            output.println(phrase);
            System.out.println("Sent: " + phrase);

            output.flush();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public String receive() {
        try {
            BufferedReader in = new BufferedReader(
                    new InputStreamReader(connection.getInputStream()));

            String phrase = in.readLine();

            if (phrase != null){
                Log.v("LOGGING", phrase);

                return phrase;
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        return "";
    }
}
