package app;
public class Main {
	static public void main(String[] args) throws InterruptedException {
		int[] numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

		// ** Início da letra a **
		MyFirstThread myThread1 = new MyFirstThread(1);
		MyFirstThread myThread2 = new MyFirstThread(2);

		myThread1.start();
		myThread1.join();
		myThread2.start();
		myThread2.join();
		// ** Fim da letra a **

		
		// ** Início da letra b ** 
		MySecondThread myThread3 = new MySecondThread(numbers, 3);

		long start = System.nanoTime();
		myThread3.start();
		myThread3.join();
		long end = System.nanoTime();
		System.out.println("Letra b) - Runtime de computePrimeFactors na thread principal: " + ((end - start)));
		// ** Fim da letra b ** 


		// ** Início da letra c ** 
		MyThirdThread myThread4 = new MyThirdThread(4);
		long tempoDeOverhead = getTempoDeOverheadDaLetraC(myThread4);
		System.out.println("Letra c) Tempo de overhead: " + tempoDeOverhead);
		// ** Fim da letra c **


		// ** Implementação da letra D está no método partitionData abaixo. ** 
		System.out.println("Letra d) - Por favor, olhar o código para ver implementação.");


		// ** Início da letra E ** 
		final int numberOfThreads = 4;
		final int workLoad = 3; 
		int[] numArray = getIntegerArray(numberOfThreads * workLoad);

		for (int i = 0; i < numberOfThreads; i++) {
			int[] localNumArray = partitionData(numArray, i * workLoad, workLoad * (i + 1) - 1);
			MyFourthThread myThread = new MyFourthThread(localNumArray, i);
			myThread.start();
		}
		// ** Fim da letra E

	}

	public static long getTempoDeOverheadDaLetraC(Thread thread) throws InterruptedException {
		long start = System.nanoTime();
		thread.start();
		thread.join();
		long end = System.nanoTime();

		return end - start;
	}

	public static int[] getIntegerArray(int number) {
		int[] numbers = new int[number];
		for (int i = 0; i < number; i++) {
			numbers[i] = i;
		}

		return numbers;
	}

	// ** Implementação da letra d **
	public static int[] partitionData(int[] values, int startIndex, int endIndex) {
		int[] numbers = new int[endIndex - startIndex + 1];
		int counter = 0;

		for (int i = startIndex; i < endIndex + 1; i++) {
			numbers[counter] = values[i];
			counter++;
		}
		return numbers;
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