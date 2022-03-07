import java.util.LinkedList;
import counter.FairSynchronizedCounter;
import thread.MyFourthThread;

public class MainLetraF {
	public static void main(String[] args) throws InterruptedException, IllegalMonitorStateException {
		// ** Início da letra F **
		FairSynchronizedCounter counter = new FairSynchronizedCounter();
		LinkedList<Thread> threads = new LinkedList<>();
		for (int i = 0; i < 10; i++) {
			threads.add(new MyFourthThread(counter));
		}

		counter.setThreads(threads);
		for (Thread threadInstance : threads) {
			threadInstance.start();
		}
		// ** Fim da letra F **
	
	}

}
