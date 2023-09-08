//jq '.[] | select(.id=="2").key'
//jq .[1].key
//jq '.[] | select(.fingerprint=="D5:1F:F8:83:C6:29:62:CE:76:7C:A6:45:E7:6C:61:5A:34:73:C8:EE")'

//use std::process::Command;
use std::fs;
use std::io::prelude::*;
use std::fs::File;
use jql::walker;
use serde_json::Value;
use std::env;

fn main() {
  let args: Vec<String> = env::args().collect();
  if args[1].trim().eq("0") {  
    let certs = "certs.json";
    let certs_file = match fs::read_to_string(certs) {
      Ok(o) => o,
      Err(e) => { println!("DB access failed: {}", e); return; }
    };
    println!("Cleaning LBB Database on certs.json...");
    let certs = "certs.json";
    let certs_file = match fs::read_to_string(certs) {
      Ok(o) => o,
      Err(e) => { println!("DB access failed: {}", e); return; }
    };
    let cleaned_str = certs_file.replace("\n","");
    let mut out_file = match File::create("out.json") {
      Ok(o) => o,
      Err(e) => { println!("File creation failed: {}", e); return; }
    };
    match out_file.write_all(cleaned_str.as_bytes()) {
      Ok(_) => (),
      Err(e) => { println!("File creation failed: {}", e); return; }
    };
    println!("Processing complete.");
  }
  if args[1].trim().eq("1") {
    let certs = "test.json";
    let certs_file = match fs::read_to_string(certs) {
      Ok(o) => o,
      Err(e) => { println!("DB access failed: {}", e); return; }
    };
    let json: Value = match serde_json::from_str(&certs) {
      Ok(o) => o,
      Err(e) => { println!("Serde failed: {}", e); return; }
    };
    let selector = Some(#r"."#);
    let selection = walker(&json, selector);
    println!("{:?}", selection);
  }
}
