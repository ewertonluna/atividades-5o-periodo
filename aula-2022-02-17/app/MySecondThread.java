package app;
import java.lang.Runnable;

/**
 * Essa classe de Thread é usada com o intuito de saber o tempo
 * de execução do método computePrimeFactors dentro da Thread.
 */
public class MySecondThread extends Thread {
	private int[] values;
	private int id;

	MySecondThread(int[] values, int id) {
		this.values = values;
		this.id = id;
	}

	@Override
	public void run() {
		long start = System.nanoTime();
		computePrimeFactors(values);
		long end = System.nanoTime();
		System.out.println("Runtime de computePrimeFactors na thread " + id + " foi de " + ((end - start)));
	}

	public static int[] computePrimeFactors(int[] values) { 
		int[] factors = new int[values.length];

		for (int i = 0; i < values.length; i++) {
			factors[i] = numPrimeFactors(values[i]); }
		return factors; 
	}
	
	public static int numPrimeFactors(int number) { 
		int primeFactors = 0;
		int n = number;
		for (int i = 2; i <= n; i++) {
			while (n % i == 0) { 
				primeFactors++;
				n /= i; }
			}
		return primeFactors; 
	}
		 
	
}
