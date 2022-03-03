public class SequentialCounter implements MyCounter {
	int value = 0;
	
	@Override
	public void increment() {
		value += 1;
	}

	@Override
	public int getValue() {
		return value;
	}
}
