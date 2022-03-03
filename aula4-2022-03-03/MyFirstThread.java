public class MyFirstThread extends Thread {
	private MyCounter myCounter;

	public MyFirstThread(MyCounter myCounter) {
		this.myCounter = myCounter;
	}

	@Override
	public void run() {
		for (int i = 0; i < 1000; i++) {
			myCounter.increment();
		}
	}
	
}
