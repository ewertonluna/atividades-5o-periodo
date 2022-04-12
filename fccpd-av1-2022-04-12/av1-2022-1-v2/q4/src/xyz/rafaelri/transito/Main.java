package xyz.rafaelri.transito;

import java.awt.BorderLayout;
import java.awt.EventQueue;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.image.BufferedImage;
import java.io.IOException;

import javax.imageio.ImageIO;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JLayeredPane;

public class Main {
	private JFrame frame;
	JLayeredPane panel;
	private ControladorCruzamento controladorCruzamento = new MeuControladorCruzamento();
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Main window = new Main();
					window.frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public Main() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frame = new JFrame();
		frame.setBounds(100, 100, 984, 696);
		frame.setResizable(false);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.getContentPane().setLayout(new BorderLayout(0, 0));
		
		JButton btnNewButton = new JButton("Esquerda");
		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				novoHorizontal();
			}
		});
		frame.getContentPane().add(btnNewButton, BorderLayout.WEST);
		
		JButton btnNewButton_1 = new JButton("Baixo");
		btnNewButton_1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				novoVertical();
			}
		});
		frame.getContentPane().add(btnNewButton_1, BorderLayout.SOUTH);
		
		panel = new JLayeredPane();
		frame.getContentPane().add(panel, BorderLayout.CENTER);
		panel.setLayout(null);
		
		JLabel lblImg = new JLabel("");
		lblImg.setBounds(0, 0, 832, 659);
		panel.add(lblImg, 1);
		BufferedImage img = null;
		try {
		    img = ImageIO.read(Main.class.getResource("/xyz/rafaelri/transito/transito.jpg"));
		    Image dimg = img.getScaledInstance(lblImg.getWidth(), lblImg.getHeight(),
		            Image.SCALE_SMOOTH);
		    lblImg.setIcon(new ImageIcon(dimg));		    
		} catch (IOException e) {
		    e.printStackTrace();
		}		
		
	}
	
	protected void novoVertical() {
	    JLabel lblNewLabel = new JLabel("");
	    lblNewLabel.setIcon(new ImageIcon(Main.class.getResource("/xyz/rafaelri/transito/caminhaov.png")));
	    lblNewLabel.setBounds(290, 650, 23, 45);
	    panel.add(lblNewLabel, 0);
	    Runnable runnable = new CaminhaoVRunnable(lblNewLabel, controladorCruzamento);
	    new Thread(runnable).start();
	}

	protected void novoHorizontal() {
	    JLabel lblNewLabel = new JLabel("");
	    lblNewLabel.setIcon(new ImageIcon(Main.class.getResource("/xyz/rafaelri/transito/caminhaoh.png")));
	    lblNewLabel.setBounds(0, 380, 45, 23);
	    panel.add(lblNewLabel, 0);
	    Runnable runnable = new CaminhaoHRunnable(lblNewLabel, controladorCruzamento);
	    new Thread(runnable).start();

	}
}
