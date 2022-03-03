public class MyFirstThread extends Thread {
	private MyCounter myCounter;
	private int id;

	public MyFirstThread(int id, MyCounter myCounter) {
		this.id = id;
		this.myCounter = myCounter;
	}

	@Override
	public void run() {
		for (int i = 0; i < 1000; i++) {
			myCounter.increment();
		}
	}
	
}
