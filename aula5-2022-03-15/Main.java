import java.io.IOException;
import java.net.UnknownHostException;
import java.util.Scanner;

import client.Client;

public class Main {
	public static void main(String[] args) throws UnknownHostException, IOException {
		Scanner scanner = new Scanner(System.in);
		Client client = new Client();
		client.startConnection("127.0.0.1", 8888);
		System.out.println("Entre com a mensagem para ser enviada ao servidor: ");
		String message = scanner.nextLine();
		String response = client.sendMessage(message);
	}
}