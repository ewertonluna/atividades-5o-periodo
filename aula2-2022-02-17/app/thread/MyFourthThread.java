package app.thread;

/**
 * Essa classe é usada para letra e
 */
public class MyFourthThread extends Thread {
	private int[] values;
	private int id;

	public MyFourthThread(int[] values, int id) {
		this.values = values;
		this.id = id;
	}

	@Override
	public void run() {
		long start = System.nanoTime();
		computePrimeFactors(values);
		long end = System.nanoTime();
		System.out.println("Letra e) - Runtime de computePrimeFactors na thread " + id + " foi de " + ((end - start)) + "ns");
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


