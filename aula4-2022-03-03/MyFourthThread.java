public class MyFourthThread extends Thread {
	private MyCounter myCounter;
	private int id;
	private Thread nextThread;

	public MyFourthThread(int id, MyCounter myCounter, Thread nextThread) {
		this.id = id;
		this.myCounter = myCounter;
		this.nextThread = nextThread;
	}

	@Override
	public void run() {
		myCounter.increment();
		nextThread.notify();
	}
	
}
