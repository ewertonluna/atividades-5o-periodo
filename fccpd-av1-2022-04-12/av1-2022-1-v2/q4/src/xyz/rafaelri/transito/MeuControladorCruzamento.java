package xyz.rafaelri.transito;

public class MeuControladorCruzamento implements ControladorCruzamento{

	@Override
	public void entrarHorizontal() {
		synchronized (this) {
			try {
				wait();
				sairHorizontal();
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}

		
	}

	@Override
	synchronized public void sairHorizontal() {
		notify();
	}
		

	@Override
	synchronized public void entrarVertical() {
			try {
				wait();
				sairVertical();
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
	}

	@Override
	synchronized public void sairVertical() {
			notify();
	}
	
}