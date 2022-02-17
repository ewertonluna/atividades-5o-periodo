package app;
public class Main {
	static public void main(String[] args) throws InterruptedException {
		int[] numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

		MyOtherThread myThread3 = new MyOtherThread();
		MyOtherThread myThread4 = new MyOtherThread();

		myThread3.run();
		myThread3.join();
		myThread4.run();
		myThread4.join();
		
		// Start clock
		int[] computedNumbers = computePrimeFactors(numbers);
		// End clock

		
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