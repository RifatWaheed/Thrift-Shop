import { BaseAuditTrailObject } from "../auditTrail/auditTrail";

export class Product extends BaseAuditTrailObject {
    pkID: number;
    name: string;
    price: number;
    stockQty: number;
    categoryID: number;
    unitID: number;
    unitName: string;
    isCombinationProduct: boolean;
    combinationProductID: number;
    decription: string;
    keywords : string;
    imageID : number;
}