package com.example.demo.controller;

import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;



@RestController
public class Controller {

	@GetMapping(value="/")
	public String sayHello() {
		return "Hello From Spring Boot App!";
	}
	
}
