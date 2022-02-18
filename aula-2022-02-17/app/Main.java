package app;
public class Main {
	static public void main(String[] args) throws InterruptedException {
		int[] numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

		MyFirstThread myThread1 = new MyFirstThread(1);
		MyFirstThread myThread2 = new MyFirstThread(2);

		myThread1.run();
		myThread1.join();
		myThread2.run();
		myThread2.join();

		MySecondThread myThread3 = new MySecondThread(numbers, 3);

		long start = System.nanoTime();
		myThread3.run();
		myThread3.join();
		long end = System.nanoTime();
		System.out.println("Runtime de computePrimeFactors na thread principal: " + ((end - start)));
		

		
		
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