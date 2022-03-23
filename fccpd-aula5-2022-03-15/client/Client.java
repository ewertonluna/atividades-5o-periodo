package client;

import java.net.*;
import java.io.*;

public class Client {
	private Socket clientSocket;
    private PrintWriter out;
    private BufferedReader in;
	private DataInputStream dataIn;
	private DataOutputStream dataOut;

    public void startConnection(String ip, int port) throws UnknownHostException, IOException {
        clientSocket = new Socket(ip, port);
        out = new PrintWriter(clientSocket.getOutputStream(), true);
        in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
		dataIn = new DataInputStream(clientSocket.getInputStream());
		dataOut = new DataOutputStream(clientSocket.getOutputStream());
    }

    public String sendMessage(String msg) throws IOException {
        out.println(msg);
        String resp = in.readLine();
        return resp;
    }

	public void askNumbers(int n) throws IOException {
		dataOut.writeInt(n);
	}

	public void logNumbers(int n) throws IOException {
		for (int i = 0; i < n; i++) {
			int number = dataIn.readInt();
			System.out.println("Client here. The server sent me the following number: " + number);
		}
	}

    public void stopConnection() throws IOException {
        in.close();
        out.close();
        clientSocket.close();
    }
}
