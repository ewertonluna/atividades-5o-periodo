import java.io.IOException;
import java.net.UnknownHostException;
import java.util.Scanner;

import client.Client;

// * Antes de fazer a execução, certifique-se que o segundo parâmetro do método start
// * da classe server.Server é false. Isso significa dizer que o servidor irá esperar
// * um tipo String.
public class MainLetraB {
	public static void main(String[] args) throws UnknownHostException, IOException {
		Scanner scanner = new Scanner(System.in);
		Client client = new Client();
		client.startConnection("127.0.0.1", 8888);
		System.out.println("Entre com a mensagem para ser enviada ao servidor: ");
		String message = scanner.nextLine();
		String response = client.sendMessage(message);
		System.out.println("Resposta devolvida do servidor: '" + response + "'");
	}
}