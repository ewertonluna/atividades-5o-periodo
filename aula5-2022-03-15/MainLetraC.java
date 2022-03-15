import java.io.IOException;
import java.net.UnknownHostException;
import java.util.Scanner;

import client.Client;

// * Antes de fazer a execução, certifique-se que o segundo parâmetro do método start
// * da classe server.Server é true. Isso significa dizer que o servidor irá esperar
// * por um tipo inteiro.
public class MainLetraC {
	public static void main(String[] args) throws UnknownHostException, IOException {
		Scanner scanner = new Scanner(System.in);
		System.out.println("Entre com a quantidade de números que você deseja solicitar do servidor: ");
		scanner.nextLine();
		Client client = new Client();
		client.startConnection("127.0.0.1", 8888);
		client.askNumbers(10);
		client.logNumbers(10);
		scanner.close();
	}
}
