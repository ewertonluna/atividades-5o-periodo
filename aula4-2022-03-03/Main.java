public class Main {
	public static void main(String[] args) throws InterruptedException {
		// // ** Início da letra b ** 
		// MyCounter myCounter = new SequentialCounter();
		// MyFirstThread myFirstThread = new MyFirstThread(0, myCounter);
		// myFirstThread.start();
		// myFirstThread.join();
		// int value1 = myCounter.getValue();
		// System.out.println("Value: " + value1);
		// // ** Fim da letra b ** 

		// // ** Início da letra c ** 
		// MyCounter mySecondCounter = new SequentialCounter();
		// for (int i = 0; i < 10; i++) {
		// 	MyFirstThread myThread = new MyFirstThread(i, mySecondCounter);
		// 	myThread.start();
		// }

		// int value2 = mySecondCounter.getValue();
		// System.out.println("Value: " + value2);
		// // ** Fim da letra c ** 
		

		// MyCounter myThirdCounter = new SafeSequentialCounter();
		// for (int i = 0; i < 10; i++) {
		// 	MyFirstThread myThread = new MyFirstThread(i, myThirdCounter);
		// 	myThread.start();
		// }
		// int value3 = myThirdCounter.getValue();
		// System.out.println("Value: " + value3);

		// // Letra d
		// MyCounter safeCounter1 = new SafeSequentialCounter();
		// MySecondThread thread = new MySecondThread(0, safeCounter1);
		// thread.start();
		// System.out.println("Value: " + safeCounter1.getValue());

		// MyCounter safeCounter2 = new SafeSequentialCounter();
		// for (int i = 0; i < 10; i++) {
		// 	MySecondThread myThread = new MySecondThread(i, safeCounter2);
		// 	myThread.start();
		// }
		// System.out.println("Value: " + safeCounter2.getValue());
		// // Fim Letra d

		MyCounter safeCounter3 = new SafeSequentialCounter();
		for (int i = 0; i < 10; i++) {
			MyThirdThread myThread = new MyThirdThread(i, safeCounter3);
			myThread.start();
		}

		/**
		 * [thread1, thread2, thread3, thread4]
		 * [thread1.wait(), thread2.wait(), thread3.wait(), thread4.wait()]
		 * Thread1(0, myCounter, lista[i + 1]) 
		 */
	
	}
}