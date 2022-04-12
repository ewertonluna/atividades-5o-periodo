package xyz.rafaelri.transito;

import javax.swing.JLabel;
import javax.swing.SwingUtilities;

public class CaminhaoVRunnable implements Runnable {

	private ControladorCruzamento controladorCruzamento;
	private JLabel label;

	CaminhaoVRunnable(JLabel label, ControladorCruzamento controladorCruzamento) {
		this.label = label;
		this.controladorCruzamento = controladorCruzamento;
	}

	public void run() {
		while (label.getY() > 0) {
			if (label.getY() == 480) {
				this.controladorCruzamento.entrarVertical();
			}
			if (label.getY() == 140) {
				this.controladorCruzamento.sairVertical();
			}
			try {
				Thread.currentThread().sleep(20);
			} catch (InterruptedException e) {
			}
			SwingUtilities.invokeLater(new Runnable () {
				public void run() {
					label.setBounds(label.getX(), label.getY()-1, label.getWidth(), label.getHeight());
				}
			});
		}
		label.setVisible(false);
	}

}
