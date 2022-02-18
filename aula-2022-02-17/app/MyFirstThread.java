package app;

/**
 * Essa classe de Thread é usada intuito o de logar no console
 * a mensagem "Hello Thread" juntamente com seu identificador.
 */
public class MyFirstThread extends Thread {
	private int id;

	MyFirstThread(int id) {
		this.id = id;
	}

	public void run() {
		System.out.println("Hello Thread! " + id);
	}

	public static int[] computePrimeFactors(int[] values) { 
		int[] factors = new int[values.length];

		for (int i = 0; i < values.length; i++) {
			factors[i] = numPrimeFactors(values[i]);
		 }
		return factors; 
	}
	
	public static int numPrimeFactors(int number) { 
		int primeFactors = 0;
		int n = number;
		for (int i = 2; i <= n; i++) {
			while (n % i == 0) { 
				primeFactors++;
				n /= i; 
			}
		}
		return primeFactors; 
	}
	
}
