import counter.ICounter;
import counter.SequentialCounter;
import thread.MyFirstThread;

public class MainLetraB {
	public static void main(String[] args) throws InterruptedException, IllegalMonitorStateException {
		// ** Início da letra b ** 
		ICounter myCounter = new SequentialCounter();
		MyFirstThread myFirstThread = new MyFirstThread(0, myCounter);
		myFirstThread.start();
		myFirstThread.join();
		int value1 = myCounter.getValue();
		System.out.println("Letra b) Value: " + value1);
		// ** Fim da letra b ** 
	}
}