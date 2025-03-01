import { PinataSDK } from "pinata-web3";
import dotenv from "dotenv";

dotenv.config(); // Load environment variables

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT,
  pinataGateway: process.env.PINATA_GATEWAY,
});

async function uploadFile() {
  try {
    const file = new File(["hellos"], "Test.txt", { type: "text/plain" });
    const upload = await pinata.upload.file(file);
    console.log(upload);
  } catch (error) {
    console.log("Upload Error:", error);
  }
}

// Add the fetchFile function to retrieve a file by CID
async function fetchFile() {
  try {
    const cid = "bafkreibm6jg3ux5qumhcn2b3flc3tyu6dmlb4xa7u5bf44yegnrjhc4yeq"; // Example CID
    const data = await pinata.gateways.get(cid);
    console.log("File Retrieved:", data);  // Logs the retrieved file data
  } catch (error) {
    console.log("Fetch Error:", error);  // Error handling for fetch
  }
}

// Uncomment to upload a file
uploadFile();

// Fetch the file after uploading (if you need to test both)
//fetchFile();
