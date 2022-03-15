package server;

import java.net.*;
import java.io.*;
import java.util.Random;

public class Server {
	private ServerSocket serverSocket;
    private Socket clientSocket;
    private PrintWriter out;
    private BufferedReader in;
	private DataInputStream dataIn;
	private DataOutputStream dataOut;

    public void start(int port, boolean isInputInteger) throws IOException {
        serverSocket = new ServerSocket(port);
        clientSocket = serverSocket.accept();
        out = new PrintWriter(clientSocket.getOutputStream(), true);
        in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
		dataIn = new DataInputStream(clientSocket.getInputStream());
		dataOut = new DataOutputStream(clientSocket.getOutputStream());

		if (isInputInteger) {
			int n = dataIn.readInt();
			int[] numbers = generateRandomNumbers(n);
			for (int i = 0; i < n; i++) {
				dataOut.writeInt(numbers[i]);
			}
		} else {
			String greeting = in.readLine();
			System.out.println("Message received from client: " + greeting);
			out.println("Hi, client. This was your message: " + greeting);
		}
    }

    public void stop() throws IOException {
        in.close();
        out.close();
		dataIn.close();
		dataOut.close();
        clientSocket.close();
        serverSocket.close();
    }

	public int[] generateRandomNumbers(int n) {
		int[] numbers = new int[n];
		Random random = new Random();
		for (int i = 0; i < numbers.length; i++) {
			numbers[i] = random.nextInt(100);
		}
		return numbers;
	}

    public static void main(String[] args) throws IOException {
        Server server = new Server();
		// ** Sete o boolean de server.start() abaixo como false para execução da letra b e como true para execução da letra c.
        server.start(8888, true);
    }
}
