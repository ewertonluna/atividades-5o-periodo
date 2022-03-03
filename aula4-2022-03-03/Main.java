public class Main {
	public static void main(String[] args) throws InterruptedException {
		MyCounter myCounter = new SequentialCounter();
		MyFirstThread myFirstThread = new MyFirstThread(myCounter);
		myFirstThread.start();
		myFirstThread.join();
		int value1 = myCounter.getValue();
		System.out.println("Value: " + value1);

		MyCounter mySecondCounter = new SequentialCounter();
		for (int i = 0; i < 10; i++) {
			MyFirstThread myThread = new MyFirstThread(mySecondCounter);
			myThread.start();
		}

		int value2 = mySecondCounter.getValue();
		System.out.println("Value: " + value2);

	}
}