package app;
import java.lang.Runnable;

public class MyThread implements Runnable{
	private String message;

	public MyThread(String message) {
		this.message = message;
	}

	@Override
	public void run() {
		System.out.println(message);
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
