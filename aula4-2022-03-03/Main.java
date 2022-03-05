import java.util.ArrayList;
import java.util.List;

import counter.ICounter;
import counter.SafeSequentialCounter;
import counter.SequentialCounter;
import thread.MyFirstThread;
import thread.MySecondThread;
import thread.MyThirdThread;

public class Main {
	public static void main(String[] args) throws InterruptedException, IllegalMonitorStateException {
		// ** Início da letra b ** 
		ICounter myCounter = new SequentialCounter();
		MyFirstThread myFirstThread = new MyFirstThread(0, myCounter);
		myFirstThread.start();
		myFirstThread.join();
		int value1 = myCounter.getValue();
		System.out.println("Value: " + value1);
		// ** Fim da letra b ** 

		// ** Início da letra c ** 
		ICounter mySecondCounter = new SequentialCounter();
		for (int i = 0; i < 10; i++) {
			MyFirstThread myThread = new MyFirstThread(i, mySecondCounter);
			myThread.start();
		}

		int value2 = mySecondCounter.getValue();
		System.out.println("Value: " + value2);
		// ** Fim da letra c ** 
		

		ICounter myThirdCounter = new SafeSequentialCounter();
		for (int i = 0; i < 10; i++) {
			MyFirstThread myThread = new MyFirstThread(i, myThirdCounter);
			myThread.start();
		}
		int value3 = myThirdCounter.getValue();
		System.out.println("Value: " + value3);

		// Letra d
		ICounter safeCounter1 = new SafeSequentialCounter();
		MySecondThread thread = new MySecondThread(0, safeCounter1);
		thread.start();
		System.out.println("Value: " + safeCounter1.getValue());

		ICounter safeCounter2 = new SafeSequentialCounter();
		for (int i = 0; i < 10; i++) {
			MySecondThread myThread = new MySecondThread(i, safeCounter2);
			myThread.start();
		}
		System.out.println("Value: " + safeCounter2.getValue());
		// Fim Letra d

		ICounter safeCounter3 = new SafeSequentialCounter();
		for (int i = 0; i < 10; i++) {
			MyThirdThread myThread = new MyThirdThread(i, safeCounter3);
			myThread.start();
		}

		// ** Início da letra F **
		// ** Fim da letra F **
	
	}
}