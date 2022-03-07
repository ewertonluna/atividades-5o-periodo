import counter.ICounter;
import counter.SequentialCounter;
import thread.MyFirstThread;

public class MainLetraC {
	
	public static void main(String[] args) throws InterruptedException, IllegalMonitorStateException {
		// ** Início da letra c ** 
		ICounter mySecondCounter = new SequentialCounter();
		for (int i = 0; i < 10; i++) {
			MyFirstThread myThread = new MyFirstThread(i, mySecondCounter);
			myThread.start();
		}

		int value2 = mySecondCounter.getValue();
		System.out.println("Value: " + value2);
		// ** Fim da letra c ** 
	}
		
}
