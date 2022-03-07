import counter.ICounter;
import counter.SafeSequentialCounter;
import thread.MySecondThread;

public class MainLetraD {
	public static void main(String[] args) throws InterruptedException, IllegalMonitorStateException {
		// ** Iniciar letra d **
		ICounter safeCounter1 = new SafeSequentialCounter();
		MySecondThread thread = new MySecondThread(0, safeCounter1);
		thread.start();
		System.out.println("Letra d) Value: " + safeCounter1.getValue());

		ICounter safeCounter2 = new SafeSequentialCounter();
		for (int i = 0; i < 10; i++) {
			MySecondThread myThread = new MySecondThread(i, safeCounter2);
			myThread.start();
		}
		System.out.println("Letra d) Value: " + safeCounter2.getValue());
		// ** Fim Letra d **
	}
}
