import { PinataSDK } from "pinata-web3";
import dotenv from "dotenv";

dotenv.config(); // Load environment variables

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT,
  pinataGateway: process.env.PINATA_GATEWAY,
});

async function uploadFile() {
  try {
    const file = new File(["hello"], "Testing.txt", { type: "text/plain" });
    const upload = await pinata.upload.file(file);
    console.log(upload);
  } catch (error) {
    console.log("Upload Error:", error);
  }
}

uploadFile();
