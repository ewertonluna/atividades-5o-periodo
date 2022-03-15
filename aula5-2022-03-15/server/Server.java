package server;

import java.net.*;
import java.io.*;
import java.util.Random;

public class Server {
	private ServerSocket serverSocket;
    private Socket clientSocket;
    private PrintWriter out;
    private BufferedReader in;

    public void start(int port) throws IOException {
        serverSocket = new ServerSocket(port);
        clientSocket = serverSocket.accept();
        out = new PrintWriter(clientSocket.getOutputStream(), true);
        in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
        String greeting = in.readLine();
		System.out.println("Message from client: " + greeting);
            // if ("hello server".equals(greeting)) {
            //     out.println("hello client");
            // }
            // else {
            //     out.println("unrecognised greeting");
            // }
    }

    public void stop() throws IOException {
        in.close();
        out.close();
        clientSocket.close();
        serverSocket.close();
    }

	public int[] generateRandomNumbers(int n) {
		int[] numbers = new int[n];
		Random random = new Random();
		for (int i = 0; i < numbers.length; i++) {
			numbers[i] = random.nextInt(10);
		}
		return numbers;
	}

    public static void main(String[] args) throws IOException {
        Server server = new Server();
        server.start(8888);
    }
}
