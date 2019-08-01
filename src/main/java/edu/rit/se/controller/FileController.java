package edu.rit.se.controller;

import org.springframework.web.bind.annotation.PostMapping;

import edu.rit.se.payload.UploadFileResponse;
import edu.rit.se.service.FileStorageService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

@RestController
public class FileController {
	@Autowired
	private FileStorageService fileStorageService;

	@PostMapping("/uploadFile")
	public UploadFileResponse uploadFile(
			@RequestParam("file") MultipartFile file) {
	
		String fileName = fileStorageService.storeFile(file);
		
		String python_path = "/Library/Frameworks/Python.framework/Versions/3.6/bin/python3";
		String script_path = "python/app.py";
		// filePath cannot contain spaces or sys.argv will not parse correctly
		String filePath = fileStorageService.getTargetLocation();
		
		
		String command = python_path + " " + script_path + " --image " + filePath + " --yolo yolo_coco";
		
		try {
			Process p = Runtime.getRuntime().exec(command);
			BufferedReader reader = new BufferedReader(
					new InputStreamReader((p.getInputStream())));
			String line;
			System.out.println("Python output is: ");
			while ((line = reader.readLine()) != null) {
				System.out.println(line);
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		
		return new UploadFileResponse(fileName,
				file.getContentType(), file.getSize());
	}

	@PostMapping("/uploadMultipleFiles")
	public List<UploadFileResponse> uploadMultipleFiles(
			@RequestParam("files") MultipartFile[] files) {
		
		return Arrays.asList(files).stream().map(file -> uploadFile(file))
				.collect(Collectors.toList());
	}
	
}
