public class MySecondThread extends Thread {
	private MyCounter myCounter;
	private int id;

	public MySecondThread(int id, MyCounter myCounter) {
		this.id = id;
		this.myCounter = myCounter;
	}

	@Override
	public void run() {
		myCounter.increment();
	}
	
}
