public class SafeSequentialCounter implements MyCounter {
	int value = 0;

	@Override
	public int getValue() {
		return value;
	}

	@Override
	public synchronized void increment() {
		value += 1;
	}
	
}
