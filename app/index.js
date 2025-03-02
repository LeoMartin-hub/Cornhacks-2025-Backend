import { PinataSDK } from "pinata-web3";
import dotenv from "dotenv";

dotenv.config();

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT,
  pinataGateway: process.env.PINATA_GATEWAY,
});

async function uploadFile() {
  try {
    const file = new File(["hellos"], "Testsdrfkg.txt", { type: "text/plain" });
    const upload = await pinata.upload.file(file);
    console.log("Upload successful:", upload);
    return upload.IpfsHash; 
  } catch (error) {
    console.log("Upload Error:", error);
    return null;
  }
}

async function fetchFile(cid) {
  try {
    if (!cid) {
      throw new Error("CID is required");
    }
    
    // Direct gateway URL format
    const gatewayUrl = process.env.PINATA_GATEWAY || "https://gateway.pinata.cloud";
    

    const url = new URL(`${gatewayUrl}/ipfs/${cid}`);
    
    console.log(`Attempting to fetch from: ${url.toString()}`);
    
    const response = await fetch(url.toString());
    
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    
    const data = await response.text();
    console.log("File Retrieved:", data);
    return data;
  } catch (error) {
    console.log("Fetch Error:", error);
    
    // More detailed error handling
    if (error.message.includes("401")) {
      console.log("Authentication issue. Please check your JWT token and gateway permissions.");
    } else if (error.message.includes("404")) {
      console.log("Content not found. The CID might not exist or might be private.");
    }
  }
}

async function main() {

    const uploadedCid = await uploadFile();
    console.log("Uploaded CID:", uploadedCid);
    
    console.log("Waiting for content to propagate...");
    await new Promise(resolve => setTimeout(resolve, 2000));
    
    if (uploadedCid) {
      await fetchFile(uploadedCid);
    }
}

main();
