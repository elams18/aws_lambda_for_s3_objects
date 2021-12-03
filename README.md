# aws_lambda_for_s3_objects
---------------------------------

This repo contains the implements of the /get-list endpoint to display the list of url of the images present in the S3 bucket.

**Get-List endpoint**: https://as1lyufcqh.execute-api.ap-south-1.amazonaws.com/get-list

### Output JSON Format
```
{
  "data": {
    "links": [
      "https://imagesbewelldigital.s3.ap-south-1.amazonaws.com/autumn_leaves_PNG3595.png",
      "https://imagesbewelldigital.s3.ap-south-1.amazonaws.com/autumn_leaves_PNG3601.png",
      "https://imagesbewelldigital.s3.ap-south-1.amazonaws.com/autumn_leaves_PNG3606.png",
      "https://imagesbewelldigital.s3.ap-south-1.amazonaws.com/autumn_leaves_PNG3607.png",
      "https://imagesbewelldigital.s3.ap-south-1.amazonaws.com/autumn_leaves_PNG3608.png",
      "https://imagesbewelldigital.s3.ap-south-1.amazonaws.com/autumn_leaves_PNG3609.png",
      "https://imagesbewelldigital.s3.ap-south-1.amazonaws.com/autumn_leaves_PNG3610.png",
      "https://imagesbewelldigital.s3.ap-south-1.amazonaws.com/autumn_leaves_PNG3611.png",
      "https://imagesbewelldigital.s3.ap-south-1.amazonaws.com/autumn_leaves_PNG3612.png",
      "https://imagesbewelldigital.s3.ap-south-1.amazonaws.com/autumn_leaves_PNG3613.png"
    ]
  },
  "status": "200",
  "Content-Type": "application/json; charset=utf-8",
  "count": 10
}
```
