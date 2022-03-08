import counter.ICounter;
import counter.SafeSequentialCounter;
import counter.SequentialCounter;
import thread.MyFirstThread;
import thread.MySecondThread;

public class MainLetraD {
	public static void main(String[] args) throws InterruptedException, IllegalMonitorStateException {
		// ** Letra d - 1a combinação **
		ICounter myCounter = new SequentialCounter();
		MyFirstThread myFirstThread = new MyFirstThread(0, myCounter);
		myFirstThread.start();
		myFirstThread.join();
		int value1 = myCounter.getValue();
		System.out.println("Letra d - 1a combinação) Value: " + value1);

		// ** Letra d - 2a combinação **
		ICounter mySecondCounter = new SequentialCounter();
		for (int i = 0; i < 10; i++) {
			MySecondThread myThread = new MySecondThread(i, mySecondCounter);
			myThread.start();
		}
		int value2 = mySecondCounter.getValue();
		System.out.println("Letra d - 2a combinação) Value: " + value2);
		
		// ** Letra d - 3a combinação **
		ICounter safeCounter1 = new SafeSequentialCounter();
		MySecondThread thread = new MySecondThread(0, safeCounter1);
		thread.start();
		System.out.println("Letra d - 3a combinação) Value: " + safeCounter1.getValue());

		// ** Letra d - 4a combinação ** 
		ICounter safeCounter2 = new SafeSequentialCounter();
		for (int i = 0; i < 10; i++) {
			MySecondThread myThread = new MySecondThread(i, safeCounter2);
			myThread.start();
		}
		System.out.println("Letra d) - 4a combinação) Value: " + safeCounter2.getValue());
	}
}
