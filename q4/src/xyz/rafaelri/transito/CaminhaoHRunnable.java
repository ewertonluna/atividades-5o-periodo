package xyz.rafaelri.transito;

import javax.swing.JLabel;
import javax.swing.SwingUtilities;

public class CaminhaoHRunnable implements Runnable {

	private ControladorCruzamento controladorCruzamento;
	private JLabel label;

	CaminhaoHRunnable(JLabel label, ControladorCruzamento controladorCruzamento) {
		this.label = label;
		this.controladorCruzamento = controladorCruzamento;
	}

	public void run() {
		while (label.getX() < 860) {
			if (label.getX() == 230) {
				this.controladorCruzamento.entrarHorizontal();
			}
			if (label.getX() == 520) {
				this.controladorCruzamento.sairHorizontal();
			}
			try {
				Thread.currentThread().sleep(20);
			} catch (InterruptedException e) {
			}
			SwingUtilities.invokeLater(new Runnable () {
				public void run() {
					label.setBounds(label.getX()+1, label.getY(), label.getWidth(), label.getHeight());
				}
			});
		}
		label.setVisible(false);
	}

}
