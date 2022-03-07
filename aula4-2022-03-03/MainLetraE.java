import counter.ICounter;
import counter.SafeSequentialCounter;
import thread.MyThirdThread;

public class MainLetraE {
	public static void main(String[] args) throws InterruptedException, IllegalMonitorStateException {
		ICounter safeCounter3 = new SafeSequentialCounter();
		for (int i = 0; i < 10; i++) {
			MyThirdThread myThread = new MyThirdThread(i, safeCounter3);
			myThread.start();
		}
	
	}

}
