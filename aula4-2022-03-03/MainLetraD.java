import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

import counter.FairSynchronizedCounter;
import counter.ICounter;
import counter.SafeSequentialCounter;
import counter.SequentialCounter;
import thread.MyFirstThread;
import thread.MyFourthThread;
import thread.MySecondThread;
import thread.MyThirdThread;

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
