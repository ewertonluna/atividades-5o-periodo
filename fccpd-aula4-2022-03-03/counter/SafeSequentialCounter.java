package counter;

// Solução da letra C
public class SafeSequentialCounter implements ICounter {
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
